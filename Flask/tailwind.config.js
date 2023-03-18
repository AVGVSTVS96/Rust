/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'], // Add the paths to your HTML files
  theme: {
    extend: {
      colors: {
        mycustom: {
          100: '#191D43',
          200: '#191D2D'
        }
      }
    },
  },
  plugins: [],
}
