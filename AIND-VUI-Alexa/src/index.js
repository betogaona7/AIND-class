'use strict';
var Alexa = require('alexa-sdk');
var APP_ID = undefined;  // can be replaced with your app ID if publishing
var facts = require('./facts');
var GET_FACT_MSG_EN = [
    "Here's your fact: ",
    "What about this one: ",
    "Okey, listen: ",
    "Yes boss, what about this: ",
    "Of course: "
]
// Test hooks - do not remove!
exports.GetFactMsg = randomPhrase(GET_FACT_MSG_EN);
var APP_ID_TEST = "mochatest";  // used for mocha tests to prevent warning
// end Test hooks

var languageStrings = {
    "en": {
        "translation": {
            "FACTS": facts.FACTS_EN,
            "SKILL_NAME": "My History Facts",  // OPTIONAL change this to a more descriptive name
            "GET_FACT_MESSAGE": GET_FACT_MSG_EN[0],
            "NO_FACT_WITH_YEAR": "Sorry, I could not find a fact of that year, but what about this...",
            "REPROMPT_MESSAGE": "You want another fact?",
            "HELP_MESSAGE": "You can say tell me a fact, or, you can say exit... What can I help you with?",
            "HELP_REPROMPT": "What can I help you with?",
            "STOP_MESSAGE": "Goodbye!"
        }
    }
};

exports.handler = function (event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    // set a test appId if running the mocha local tests
    if (event.session.application.applicationId == "mochatest") {
        alexa.appId = APP_ID_TEST
    }
    // To enable string internationalization (i18n) features, set a resources object.
    alexa.resources = languageStrings;
    alexa.registerHandlers(handlers);
    alexa.execute();
};

var handlers = {
    'LaunchRequest': function () {
        this.emit('GetFact');
    },
    'GetNewFactIntent': function () {
        this.emit('GetFact');
    },
    'GetFact': function () {
        // Get a random fact from the facts list
        // Use this.t() to get corresponding language data
        var factArr = this.t('FACTS');
        var randomFact = randomPhrase(factArr);

        // Create speech output
        var speechOutput = this.t("GET_FACT_MESSAGE") + randomFact;
        var repromptMessage = this.t("REPROMPT_MESSAGE");
        this.emit(':askWithCard', speechOutput, repromptMessage, this.t("SKILL_NAME"), randomFact);
    },
    'GetNewYearFactIntent': function () {
        //TODO your code here
        var factArray = this.t('FACTS');
        var year = this.event.request.intent.slots['FACT_YEAR'].value;
        if(year){
            var fact = "";
            for(var i = 0; i < factArray.length; i++){
                if(factArray[i].includes(year)){
                    fact = factArray[i];
                    break;
                }
            }
            if (fact.length == 0){
                var randomFact = randomPhrase(factArray);
                var speechOutput = this.t("NO_FACT_WITH_YEAR") + randomFact;
                var repromptMessage = this.t("REPROMPT_MESSAGE");
                this.emit(':askWithCard', speechOutput, repromptMessage, this.t("SKILL_NAME"), randomFact);
            }else{
                var speechOutput = this.t("GET_FACT_MESSAGE") + fact;
                var repromptMessage = this.t("REPROMPT_MESSAGE");
                this.emit(':askWithCard', speechOutput, repromptMessage, this.t("SKILL_NAME"), fact);
            }

        }else{
            var randomFact = randomPhrase(factArray);
            var speechOutput = this.t("GET_FACT_MESSAGE") + randomFact;
            this.emit(':tellWithCard', speechOutput, this.t("SKILL_NAME"), randomFact);
        }

    },
    'AMAZON.HelpIntent': function () {
        var speechOutput = this.t("HELP_MESSAGE");
        var reprompt = this.t("HELP_MESSAGE");
        this.emit(':ask', speechOutput, reprompt);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', this.t("STOP_MESSAGE"));
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', this.t("STOP_MESSAGE"));
    }
};

function randomPhrase(phraseArr) {
    // returns a random phrase
    // where phraseArr is an array of string phrases
    var i = 0;
    i = Math.floor(Math.random() * phraseArr.length);
    return (phraseArr[i]);
};
