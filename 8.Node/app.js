const express = require('express')

const app = express()

app.get('/', (req, res) => {
    res.send('hello, world form node.js')
})

app.listen(3000, () => {
    console.log('서버가 준비되었음.')
})