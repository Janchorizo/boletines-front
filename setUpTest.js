const mockFetchPromise = () => {
  return Promise.resolve({})
}

global.fetch = jest.fn(() => mockFetchPromise())
