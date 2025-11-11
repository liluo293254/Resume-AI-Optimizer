import { useState } from 'react'
import ResumeOptimizer from './components/ResumeOptimizer'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI 智能简历优化器</h1>
        <p>使用AI技术优化您的简历，提升求职成功率</p>
      </header>
      <main>
        <ResumeOptimizer />
      </main>
    </div>
  )
}

export default App

