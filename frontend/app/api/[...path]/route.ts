import { NextRequest, NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://127.0.0.1:8000'

export async function GET(
  request: NextRequest,
  { params }: { params: { path: string[] } }
) {
  const path = params.path.join('/')
  const url = new URL(request.url)
  const queryString = url.search
  
  console.log(`Proxying GET request to: ${BACKEND_URL}/${path}${queryString}`)
  console.log(`Environment: ${process.env.NODE_ENV}, Backend URL: ${BACKEND_URL}`)
  
  try {
    const response = await fetch(`${BACKEND_URL}/${path}${queryString}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      signal: AbortSignal.timeout(10000), // 10 second timeout
    })
    
    const data = await response.json()
    console.log(`Backend response status: ${response.status}`)
    return NextResponse.json(data, { status: response.status })
  } catch (error) {
    console.error('Backend connection error:', error)
    return NextResponse.json(
      { error: 'Backend service unavailable', details: error instanceof Error ? error.message : String(error) },
      { status: 503 }
    )
  }
}

export async function POST(
  request: NextRequest,
  { params }: { params: { path: string[] } }
) {
  const path = params.path.join('/')
    const body = await request.json()
  
  console.log(`Proxying POST request to: ${BACKEND_URL}/${path}`)
  console.log(`Environment: ${process.env.NODE_ENV}, Backend URL: ${BACKEND_URL}`)
  console.log(`Request body:`, body)
  console.log(`Body type:`, typeof body)
  
  // Ensure body is properly formatted
  const requestBody = typeof body === 'string' ? body : JSON.stringify(body)
  
  try {
    const response = await fetch(`${BACKEND_URL}/${path}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: requestBody,
      signal: AbortSignal.timeout(10000), // 10 second timeout
    })
    
    const data = await response.json()
    console.log(`Backend response status: ${response.status}`)
    return NextResponse.json(data, { status: response.status })
  } catch (error) {
    console.error('Backend connection error:', error)
    return NextResponse.json(
      { error: 'Backend service unavailable', details: error instanceof Error ? error.message : String(error) },
      { status: 503 }
    )
  }
} 