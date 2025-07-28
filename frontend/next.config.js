/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    outputFileTracingRoot: undefined,
  },
  output: 'standalone',
  telemetry: false,
}

module.exports = nextConfig 