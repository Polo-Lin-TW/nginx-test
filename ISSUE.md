# Issues and Solutions

## Issue #1: Backend Connection Failed - JSON Parsing Error

### 問題描述
執行 `testBackend` 函式時出現以下錯誤訊息：
```
Backend connection failed: Unexpected token '<', "<!DOCTYPE "... is not valid JSON
```

### 解決方案

**步驟 1**: 創建開發專用的 Dockerfile
```dockerfile
# frontend/Dockerfile.dev
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose port 3000 for Vite dev server
EXPOSE 3000

# Start Vite development server
CMD ["npm", "run", "dev"]
```

**步驟 2**: 配置 Vite 代理設定
```javascript
// frontend/vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://backend:8000',  // 使用 Docker 服務名稱
        changeOrigin: true,
        secure: false
      }
    }
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets'
  }
})
```

**步驟 3**: 修改 docker-compose.yml 配置
```yaml
# Vue 3 Frontend (for development)
frontend-dev:
  build:
    context: ./frontend
    dockerfile: Dockerfile.dev  # 使用開發版 Dockerfile
  container_name: nginx-demo-frontend-dev
  ports:
    - "3000:3000"              # 端口映射改為 3000:3000
  volumes:
    - ./frontend:/app          # 代碼熱重載
    - /app/node_modules
  depends_on:
    - backend
  restart: unless-stopped
  profiles:
    - dev
```

**步驟 4**: 簡化前端 API 調用
```javascript
// frontend/src/App.vue - testBackend 方法
async testBackend() {
  this.loading = true
  this.backendStatus = null
  
  try {
    // 使用相對路徑，由 Vite 代理處理
    const response = await fetch('/api/health')
    if (response.ok) {
      const data = await response.json()
      this.backendStatus = {
        success: true,
        message: `✅ Backend connected: ${data.status}`
      }
    } else {
      throw new Error(`HTTP ${response.status}`)
    }
  } catch (error) {
    this.backendStatus = {
      success: false,
      message: `❌ Backend connection failed: ${error.message}`
    }
  } finally {
    this.loading = false
  }
}
```

### 重啟服務
```bash
docker-compose --profile dev down
docker-compose --profile dev up --build -d
```

### 驗證
- 訪問: http://localhost:3000
- 點擊 "Test Backend API" 按鈕
- 應顯示: "✅ Backend connected: healthy"