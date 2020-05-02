const webpackConfig = require('./webpack.config.js')
const path = require('path')
const CopyPlugin = require('copy-webpack-plugin')
const outputDir = 'dist'

var config = Object.assign({}, webpackConfig, {
  plugins: [
    new CopyPlugin([
      { from: 'statics', to: path.join(__dirname, outputDir, 'statics') },
      { from: 'src/index/prod/index.html', to: path.join(__dirname, outputDir) }
    ])
  ]
})

module.exports = config
