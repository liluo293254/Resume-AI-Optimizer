import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface OptimizeResumeResponse {
  success: boolean
  optimized_content: string
  notes: string
}

export const optimizeResume = async (
  content: string,
  jobDescription?: string
): Promise<OptimizeResumeResponse> => {
  const response = await api.post<OptimizeResumeResponse>('/resume/optimize', {
    content,
    job_description: jobDescription,
  })
  return response.data
}

export const createResume = async (originalContent: string, jobDescription?: string) => {
  const response = await api.post('/resume/', {
    original_content: originalContent,
    job_description: jobDescription,
  })
  return response.data
}

export const getResume = async (id: number) => {
  const response = await api.get(`/resume/${id}`)
  return response.data
}

export const listResumes = async () => {
  const response = await api.get('/resume/')
  return response.data
}

export const optimizeResumeById = async (id: number) => {
  const response = await api.post(`/resume/${id}/optimize`)
  return response.data
}

export const deleteResume = async (id: number) => {
  const response = await api.delete(`/resume/${id}`)
  return response.data
}

export const healthCheck = async () => {
  const response = await api.get('/health')
  return response.data
}

