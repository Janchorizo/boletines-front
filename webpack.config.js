const path = require('path')
const CopyPlugin = require('copy-webpack-plugin')

const outputDir = 'dist'

module.exports = {
  entry: path.join(__dirname, 'src/index.js'),
  output: {
    path: path.join(__dirname, outputDir)
  },
  plugins: [
    new CopyPlugin([
      { from: 'public', to: path.join(__dirname, outputDir, 'public') },
      { from: 'src/index.html', to: path.join(__dirname, outputDir) }
    ])
  ],
  resolve: {
    alias: {
      vendor_css: path.join(__dirname, '/node_modules/spectre.css/dist/spectre.min.css'),
      common: path.join(__dirname, '/src/common/'),
      helpers: path.join(__dirname, '/src/common/helpers/'),
      components: path.join(__dirname, '/src/components/'),
      containers: path.join(__dirname, '/src/containers/'),
      app_redux: path.join(__dirname, '/src/redux/'),
      theme: path.join(__dirname, '/src/common/styles/theme.css'),
      fonts: path.join(__dirname, '/src/common/styles/fonts.css'),
    }
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /^(?!.*?\.module).*\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.module\.css$/,
        use: ['style-loader', {
          loader: 'css-loader',
          options: {
            modules: true
          }
        }]
      },
      {
        test: /\.png$/,
        use: ['file-loader']
      },
      {test: /\.(eot|svg|ttf|woff|woff2)$/, loader: 'file-loader?name=[name].[ext]'}
    ]
  },
  devServer: {
    port: 3000,
    historyApiFallback: true
  },
  devtool: 'cheap-module-source-map'
}
