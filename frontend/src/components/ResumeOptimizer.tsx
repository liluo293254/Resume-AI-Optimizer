import { useState } from 'react'
import { optimizeResume } from '../services/api'
import './ResumeOptimizer.css'

const ResumeOptimizer = () => {
  const [originalContent, setOriginalContent] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [optimizedContent, setOptimizedContent] = useState('')
  const [notes, setNotes] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleOptimize = async () => {
    if (!originalContent.trim()) {
      setError('请输入简历内容')
      return
    }

    setLoading(true)
    setError('')
    setOptimizedContent('')
    setNotes('')

    try {
      const result = await optimizeResume(originalContent, jobDescription)
      setOptimizedContent(result.optimized_content)
      setNotes(result.notes || '')
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || '优化失败，请重试')
    } finally {
      setLoading(false)
    }
  }

  const handleClear = () => {
    setOriginalContent('')
    setJobDescription('')
    setOptimizedContent('')
    setNotes('')
    setError('')
  }

  return (
    <div className="resume-optimizer">
      <div className="optimizer-container">
        <div className="input-section">
          <div className="form-group">
            <label htmlFor="resume">简历内容 *</label>
            <textarea
              id="resume"
              value={originalContent}
              onChange={(e) => setOriginalContent(e.target.value)}
              placeholder="请粘贴您的原始简历内容..."
              rows={15}
            />
          </div>

          <div className="form-group">
            <label htmlFor="job">职位描述（可选）</label>
            <textarea
              id="job"
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="请输入目标职位描述，AI将根据职位要求优化简历..."
              rows={8}
            />
          </div>

          <div className="button-group">
            <button
              onClick={handleOptimize}
              disabled={loading || !originalContent.trim()}
              className="btn-optimize"
            >
              {loading ? '优化中...' : '开始优化'}
            </button>
            <button onClick={handleClear} className="btn-clear">
              清空
            </button>
          </div>

          {error && <div className="error-message">{error}</div>}
        </div>

        <div className="output-section">
          <div className="form-group">
            <label>优化后的简历</label>
            <textarea
              value={optimizedContent}
              readOnly
              placeholder="优化后的简历将显示在这里..."
              rows={15}
              className={optimizedContent ? 'optimized' : ''}
            />
          </div>

          {notes && (
            <div className="notes-section">
              <h3>优化建议</h3>
              <p>{notes}</p>
            </div>
          )}

          {optimizedContent && (
            <div className="action-buttons">
              <button
                onClick={() => {
                  navigator.clipboard.writeText(optimizedContent)
                  alert('已复制到剪贴板')
                }}
                className="btn-copy"
              >
                复制优化结果
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default ResumeOptimizer

