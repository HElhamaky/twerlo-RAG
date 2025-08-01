import { NextRequest, NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000'

export async function GET(
  request: NextRequest,
  { params }: { params: { path: string[] } }
) {
  const path = params.path.join('/')
  const url = new URL(request.url)
  const queryString = url.search
  
  console.log(`Proxying GET request to: ${BACKEND_URL}/${path}${queryString}`)
  
  try {
    const response = await fetch(`${BACKEND_URL}/${path}${queryString}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    const data = await response.json()
    console.log(`Backend response status: ${response.status}`)
    return NextResponse.json(data, { status: response.status })
  } catch (error) {
    console.error('Backend connection error:', error)
    return NextResponse.json(
      { error: 'Backend service unavailable', details: error.message },
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
  
  try {
    const response = await fetch(`${BACKEND_URL}/${path}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...Object.fromEntries(request.headers.entries()),
      },
      body: JSON.stringify(body),
    })
    
    const data = await response.json()
    console.log(`Backend response status: ${response.status}`)
    return NextResponse.json(data, { status: response.status })
  } catch (error) {
    console.error('Backend connection error:', error)
    return NextResponse.json(
      { error: 'Backend service unavailable', details: error.message },
      { status: 503 }
    )
  }
} 