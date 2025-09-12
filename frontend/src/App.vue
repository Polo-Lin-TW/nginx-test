<template>
  <div id="app">
    <header class="header">
      <h1>Nginx Demo Web App</h1>
      <p>Vue 3 + FastAPI + Nginx</p>
    </header>
    
    <main class="main">
      <div class="card">
        <h2>Frontend Status</h2>
        <p class="status success">✅ Vue 3 Application Running</p>
      </div>
      
      <div class="card">
        <h2>Backend Connection</h2>
        <button @click="testBackend" :disabled="loading" class="test-btn">
          {{ loading ? 'Testing...' : 'Test Backend API' }}
        </button>
        <p v-if="backendStatus" :class="['status', backendStatus.success ? 'success' : 'error']">
          {{ backendStatus.message }}
        </p>
      </div>
      
      <div class="card">
        <h2>Application Info</h2>
        <ul class="info-list">
          <li><strong>Frontend:</strong> Vue 3 with Vite</li>
          <li><strong>Backend:</strong> FastAPI</li>
          <li><strong>Proxy:</strong> Nginx</li>
          <li><strong>Context7:</strong> Integrated for documentation</li>
        </ul>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      loading: false,
      backendStatus: null
    }
  },
  methods: {
    async testBackend() {
      this.loading = true
      this.backendStatus = null
      
      try {
        // Use proxy for API requests
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
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

#app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  text-align: center;
  color: white;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.header p {
  font-size: 1.2rem;
  opacity: 0.9;
}

.main {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.card h2 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.status {
  padding: 10px 15px;
  border-radius: 5px;
  font-weight: bold;
  margin-top: 15px;
}

.status.success {
  background-color: #d4edda;
  color: #155724;
}

.status.error {
  background-color: #f8d7da;
  color: #721c24;
}

.test-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
  transition: transform 0.2s ease;
}

.test-btn:hover:not(:disabled) {
  transform: scale(1.05);
}

.test-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.info-list {
  list-style: none;
}

.info-list li {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.info-list li:last-child {
  border-bottom: none;
}

.info-list strong {
  color: #667eea;
}
</style>