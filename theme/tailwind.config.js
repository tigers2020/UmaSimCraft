/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './static_src/src/**/*.{html,js}',
    '../templates/**/*.html',
    '../simulation/templates/**/*.html',
    '../restapi/templates/**/*.html',
    '../websocket/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Noto Sans KR', 'system-ui', 'sans-serif'],
      },
      colors: {
        'uma-blue': '#3B82F6',
        'uma-green': '#10B981',
        'uma-yellow': '#F59E0B',
        'uma-red': '#EF4444',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
} 