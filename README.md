# Dinosaur App - Deno with React Tutorial

A tutorial project demonstrating how to build and run a modern React application using Deno as the runtime. This dinosaur encyclopedia showcases the integration of React, TypeScript, Vite, and Deno in a full-stack application.

**This is an educational tutorial designed to help developers understand how to set up and run React projects with Deno**

## Features

- 🦕 Browse a comprehensive list of dinosaurs
- 📖 View detailed descriptions for each dinosaur species
- 🚀 Fast and responsive user interface
- 🔍 Clean, modern design with React Router navigation
- ⚡ Hot module replacement (HMR) for development

## Tech Stack

- **Runtime**: Deno (instead of Node.js)
- **Frontend**: React 19 + TypeScript + Vite
- **Backend**: Deno + Oak Framework
- **Routing**: React Router DOM
- **Development**: Hot Module Replacement (HMR)
- **Linting**: ESLint with TypeScript support

## Getting Started

### Prerequisites

- [Deno](https://deno.com/) (latest version) - **Note: Node.js is NOT required for this project**

### Tutorial Steps

1. **Clone this repository** to follow along with the tutorial
2. **Navigate to the project directory**
3. **Explore the project structure** to understand how Deno integrates with React
4. **Start the development servers:**

```bash
deno task dev
```

This will start both the API server (port 8000) and the Vite dev server (port 5173).

Alternatively, you can start them separately:

```bash
# Start the API server
deno task dev:api

# Start the frontend dev server
deno task dev:vite
```

### Available Scripts

- `deno task dev` - Start both API and frontend servers
- `deno task dev:api` - Start only the API server
- `deno task dev:vite` - Start only the frontend dev server
- `deno task build` - Build the app for production
- `deno task lint` - Run ESLint
- `deno task preview` - Preview the production build

## Project Structure

```text
├── api/
│   ├── main.ts          # Deno API server with Oak
│   └── data.json        # Dinosaur data
├── src/
│   ├── pages/
│   │   ├── index.tsx    # Homepage with dinosaur list
│   │   └── Dinosaur.tsx # Individual dinosaur details
│   ├── types.ts         # TypeScript type definitions
│   └── ...
├── deno.json           # Deno configuration
├── package.json        # NPM dependencies for frontend
└── vite.config.ts      # Vite configuration
```

## Tutorial Highlights

### Key Deno Features Demonstrated

1. **deno.json Configuration**: See how Deno replaces package.json for task management
2. **TypeScript Native Support**: No build step required for TypeScript in the backend
3. **Permission Model**: API server runs with specific permissions (--allow-net, --allow-read)
4. **Modern Import Maps**: Direct URL imports and import maps for dependency management
5. **Vite Integration**: How Vite proxy works with Deno backend services

### Learning Notes

- The `api/main.ts` file shows a Deno server using Oak framework
- Vite configuration includes proxy settings to communicate with the Deno API
- Both frontend and backend are managed through Deno tasks, not npm scripts
- This demonstrates how Deno can replace Node.js entirely in full-stack JavaScript development

## API Endpoints

- `GET /api/dinosaurs` - Get all dinosaurs
- `GET /api/dinosaurs/:name` - Get a specific dinosaur by name
