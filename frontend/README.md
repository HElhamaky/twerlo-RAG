# Twerlo Frontend

A modern Next.js application for AI-powered document chat with authentication and file upload capabilities.

## Features

### 🔐 Authentication
- **Login/Signup System**: Secure user authentication with JWT tokens
- **Protected Routes**: Automatic redirection for unauthenticated users
- **Session Management**: Persistent login state with localStorage

### 💬 Chat Interface
- **Real-time Chat**: Interactive chat interface with AI responses
- **Message History**: Persistent conversation history
- **Typing Indicators**: Visual feedback during AI processing
- **Keyboard Shortcuts**: Enter to send, Shift+Enter for new lines

### 📁 Document Management
- **File Upload**: Support for PDF, TXT, DOC, DOCX files
- **Multiple Files**: Upload multiple documents simultaneously
- **File Preview**: View uploaded files with metadata
- **Progress Tracking**: Visual upload progress indicators

### 🎨 Modern UI/UX
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark/Light Mode**: Clean, modern interface
- **Loading States**: Smooth loading animations
- **Error Handling**: User-friendly error messages

## Tech Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **State Management**: React Hooks
- **HTTP Client**: Fetch API
- **Form Handling**: React Hook Form
- **Validation**: Zod

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running on `http://localhost:8000`

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Environment Variables

Create a `.env.local` file in the frontend directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Project Structure

```
frontend/
├── app/                    # Next.js App Router pages
│   ├── chat/              # Chat interface
│   ├── login/             # Login page
│   ├── signup/            # Signup page
│   ├── globals.css        # Global styles
│   └── layout.tsx         # Root layout
├── components/            # Reusable components
│   ├── ui/               # UI components
│   │   ├── Button.tsx    # Button component
│   │   ├── Input.tsx     # Input component
│   │   └── Loading.tsx   # Loading spinner
│   ├── auth/             # Authentication components
│   ├── chat/             # Chat components
│   └── upload/           # Upload components
├── lib/                  # Utility functions
│   └── utils.ts          # Class name utilities
└── public/               # Static assets
```

## API Integration

The frontend integrates with the following backend endpoints:

### Authentication
- `POST /auth/login` - User login
- `POST /auth/register` - User registration

### Documents
- `GET /documents/` - List uploaded documents
- `POST /documents/upload` - Upload new documents

### Chat
- `POST /qa/ask` - Ask questions about documents

## Key Components

### Authentication Flow
1. User visits the app → redirected to login if not authenticated
2. Login/Signup → JWT token stored in localStorage
3. Protected routes check for valid token
4. Logout clears token and redirects to login

### Chat Flow
1. Upload documents via sidebar
2. Ask questions in chat interface
3. AI processes documents and responds
4. Conversation history maintained

### File Upload Flow
1. User selects files via file picker
2. Files uploaded to backend with progress tracking
3. Uploaded files listed in sidebar
4. Files available for AI chat queries

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

### Code Style

- TypeScript for type safety
- Tailwind CSS for styling
- Component-based architecture
- Custom hooks for reusable logic

## Deployment

### Build for Production

```bash
npm run build
npm run start
```

### Environment Setup

Ensure the backend API is running and accessible at the configured URL.

## Contributing

1. Follow the existing code style
2. Add TypeScript types for new components
3. Test authentication and chat flows
4. Ensure responsive design works on all devices

## Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure backend allows requests from frontend origin
2. **Authentication Issues**: Check JWT token format and expiration
3. **File Upload Failures**: Verify file size limits and supported formats
4. **API Connection**: Confirm backend is running on correct port

### Debug Mode

Enable debug logging by setting `NODE_ENV=development` and check browser console for detailed error messages. 