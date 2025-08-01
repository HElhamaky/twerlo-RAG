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
        'Authorization': request.headers.get('authorization') || '',
      },
      signal: AbortSignal.timeout(10000), // 10 second timeout
    })
    
    console.log(`Backend response status: ${response.status}`)
    
    // Check if response is JSON
    const contentType = response.headers.get('content-type')
    if (contentType && contentType.includes('application/json')) {
      const data = await response.json()
      return NextResponse.json(data, { status: response.status })
    } else {
      // Handle non-JSON responses (like HTML error pages)
      const text = await response.text()
      console.log(`Non-JSON response:`, text.substring(0, 200))
      return NextResponse.json(
        { error: 'Backend returned non-JSON response', details: text.substring(0, 500) },
        { status: response.status }
      )
    }
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
  
  console.log(`Proxying POST request to: ${BACKEND_URL}/${path}`)
  console.log(`Environment: ${process.env.NODE_ENV}, Backend URL: ${BACKEND_URL}`)
  
  // Check if this is a file upload (multipart/form-data)
  const contentType = request.headers.get('content-type') || ''
  
  if (contentType.includes('multipart/form-data')) {
    // Handle file upload
    console.log('Handling file upload...')
    
    try {
      const formData = await request.formData()
      
      const response = await fetch(`${BACKEND_URL}/${path}`, {
        method: 'POST',
        headers: {
          'Authorization': request.headers.get('authorization') || '',
        },
        body: formData,
        signal: AbortSignal.timeout(180000), // 3 minute timeout for uploads
      })
      
      console.log(`Backend response status: ${response.status}`)
      
      // Check if response is JSON
      const responseContentType = response.headers.get('content-type')
      if (responseContentType && responseContentType.includes('application/json')) {
        const data = await response.json()
        return NextResponse.json(data, { status: response.status })
      } else {
        // Handle non-JSON responses
        const text = await response.text()
        console.log(`Non-JSON response:`, text.substring(0, 200))
        return NextResponse.json(
          { error: 'Backend returned non-JSON response', details: text.substring(0, 500) },
          { status: response.status }
        )
      }
    } catch (error) {
      console.error('File upload error:', error)
      
      // Handle timeout errors specifically
      if (error instanceof Error && error.name === 'TimeoutError') {
        return NextResponse.json(
          { error: 'File upload timed out. Please try with a smaller file or check your connection.', details: 'Upload timeout after 3 minutes' },
          { status: 408 }
        )
      }
      
      return NextResponse.json(
        { error: 'File upload failed', details: error instanceof Error ? error.message : String(error) },
        { status: 500 }
      )
    }
  } else {
    // Handle regular JSON requests
    const body = await request.json()
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
    
      console.log(`Backend response status: ${response.status}`)
      
      // Check if response is JSON
      const responseContentType = response.headers.get('content-type')
      if (responseContentType && responseContentType.includes('application/json')) {
        const data = await response.json()
        return NextResponse.json(data, { status: response.status })
      } else {
        // Handle non-JSON responses (like HTML error pages)
        const text = await response.text()
        console.log(`Non-JSON response:`, text.substring(0, 200))
        return NextResponse.json(
          { error: 'Backend returned non-JSON response', details: text.substring(0, 500) },
          { status: response.status }
        )
      }
    } catch (error) {
      console.error('Backend connection error:', error)
      return NextResponse.json(
        { error: 'Backend service unavailable', details: error instanceof Error ? error.message : String(error) },
        { status: 503 }
      )
    }
  }
} 