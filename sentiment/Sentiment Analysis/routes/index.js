const express = require('express')
const app=express();

app.use(express.static('public'));
const router = express.Router()
const SW = require('stopword')
const natural = require('natural')
const aposToLexForm = require('apos-to-lex-form')
const SpellCorrector = require('spelling-corrector')
const spellCorrector = new SpellCorrector()
spellCorrector.loadDictionary()

module.exports.initialize = function(app) {
  app.use('/',
    router.get('/:word', async (req, res) => {
      // Filter Word
      const reviewText = req.params.word
      const lexedReview = aposToLexForm(reviewText)
      const alphaOnlyReview = lexedReview.toLowerCase().replace(/[^a-zA-Z\s]+/g, '')
      const tokenizedReview = new natural.WordTokenizer().tokenize(alphaOnlyReview)
      tokenizedReview.forEach((word, index) => tokenizedReview[index] = spellCorrector.correct(word))
      const filteredReview = SW.removeStopwords(tokenizedReview)

      // Analysis
      const analyzer = new natural.SentimentAnalyzer('English', natural.PorterStemmer, 'afinn')
      const analysis = analyzer.getSentiment(filteredReview)
      const response = analysis > 0 ? 'positive' : analysis < 0 ? 'negative' : 'neutral'
      //const myWindow = window.open();
      // Response
      if(response=='negative')
      {
        return res.send("The complaint posted by the student is Negative");
      }
      else if(response=='positive')
      {
        return res.send("The complaint posted by the student is Positive");
      }
      else
      {
        return res.send("The complaint posted by the student is Neutral");
      }
      

      
      
    })
  )
}