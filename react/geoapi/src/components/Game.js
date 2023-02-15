import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField'
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import axios from 'axios'
import Riddle from './Riddle';
import Results from './Results';
import Strikes from './Strikes';



const useStyles = makeStyles((theme) => ({

    riddleFirst: {
        borderBottom: `1px solid black`,
    },
    riddleSecond: {
        borderBottom: `1px solid black`,
    },
    riddleHeader:{

        fontSize: '32px',
        textAlign: 'center',
    },
    riddleNumberOfCountries:{
        fontSize: '28px',
        textAlign: 'center',   
    },

	suggestion: {

		cursor: 'pointer',
        borderLeft: '1px solid black',
        borderRight: '1px solid black',
        borderBottom: '1px solid black',
        borderTop: '1px solid black',
        background: 'white',
        '&:hover': {
            background: "gray",
        }
	},

    listResults: {
        padding: '0px',
    }, 

    incorrect: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '24px',
        textAlign: 'center',
        marginBottom:  '0px',
        color: 'red',
        borderColor: 'red',
        borderLeft: '1px solid ',
        borderRight: '1px solid ',
        borderBottom: '1px solid ',
        borderTop: '1px solid ',
    }, 

    correct: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '24px',
        textAlign: 'center',
        marginBottom:  '0px',
        color: 'green',
        borderColor: 'green',
        borderLeft: '1px solid ',
        borderRight: '1px solid ',
        borderBottom: '1px solid ',
        borderTop: '1px solid ',
    },

    blank: {
        
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '24px',
        textAlign: 'center',
        marginBottom: '0px',
        color: 'black',
        borderColor: 'black',
        borderLeft: '1px solid ',
        borderRight: '1px solid ',
        borderBottom: '1px solid ',
        borderTop: '1px solid ',
    }, 

    winner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '32px',
        textAlign: 'center',
        marginBottom:  '0px',
        color: 'green',
        borderColor: 'green',
        borderLeft: '1px solid ',
        borderRight: '1px solid ',
        borderBottom: '1px solid ',
        borderTop: '1px solid ',
    },

    loser: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '32px',
        textAlign: 'center',
        marginBottom:  '0px',
        color: 'red',
        borderColor: 'red',
        borderLeft: '1px solid ',
        borderRight: '1px solid ',
        borderBottom: '1px solid ',
        borderTop: '1px solid ',
    },

    hidden :
    {
        display: 'none'
    }


}));

function toTitleCase(str) {
    return str.toLowerCase().split(' ').map(function (word) {
      return (word.charAt(0).toUpperCase() + word.slice(1));
    }).join(' ');
  }

const Game = (props) => {

    const { answers, countries } = props;
    const [strikes] = useState([])
	const [text, setText] = useState([])
    const [showGuess, setShowGuess] = useState([])
    const [suggestions, setSuggestions] = useState([])
    const [history, setHistory] = useState([])
    const [guessHidden, setGuessHidden] = useState([])
    const [finished, setFinished] = useState([])
    const [boolError, setBoolError] = useState(false)
    const [helpertext, setHelpertext] = useState([])
    const [headerText, setHeaderText] = useState('Remaining: ' + (answers.answers.length+strikes.length-history.length) + ' Countries  || ' + (3 -strikes.length) + ' Strikes')
    
    const classes = useStyles();
    const [riddleHeaderClass, setRiddleHeaderClass] = useState(classes.riddleNumberOfCountries)
    

    const onSuggestHandler = (text)=>{

        setText(text);
        setSuggestions([]);
    }
	const onChangeHandler = (text) => {
        setBoolError(false)
        setHelpertext('')
        let matches = []
        if (text.length > 0) {
            matches = countries.filter(country => {
            const regex = new RegExp(`${text}`, "gi");
            return country.name.match(regex)
        })
        }

		setSuggestions(matches.slice(0,5))
        setText(text)
        
	}

    const handleSubmit = (e) => {
        e.preventDefault();
        let submittedText = toTitleCase(text.trim())

        if (history.includes(submittedText)){
            setBoolError(true)
            setHelpertext('Already Guessed')
            return
        }

        let countryValidation 
        countryValidation = countries.filter(country => {

            const regex = new RegExp(`^${submittedText}$`, "i");
            return (country.name.match(regex))
        })

        if (countryValidation.length===0){
            setBoolError(true)
            setHelpertext('Enter a valid country')
            setText('')

            return
        }

        history.push(submittedText)
        // let config = {
        //     headers: {
        //       'Set-Cookie': 'sessionid=lw72b2vff48m0ivsdw6fiwuhxtwdruy2; expires=Wed, 01 Mar 2023 20:02:58 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax',
        //     }
        //   }
          
        axios.post('http://127.0.0.1:8000/api/riddles/' + answers.id +'/', {
        
        // Not sure if this tbelongs here
        'country': submittedText
          }, { withCredentials: true });
    

        let isStrike = true
        for (var i = 0; i < answers.answers.length; i++){
            if (answers.answers[i].name === submittedText){
                isStrike = false
            }

        }

        if (isStrike === true){
            strikes.push(submittedText)
    
            if  (strikes.length===3) {
                setFinished('Lost')
                setHeaderText('You Loser!')
                setRiddleHeaderClass(classes.loser)
                setHistory([])
                setShowGuess(false)
            }
            setText('')
            return
        }
    
        if ((answers.answers.length+strikes.length-history.length)===0 ){
            setFinished('Won')
            setHeaderText('Winner')
            setRiddleHeaderClass(classes.winner)
            setHistory([])
            setShowGuess(false)
            
    
        }
    
        setText('')
        return
    }

	if (!answers || answers.length === 0) return <p>Can not find any answers, sorry</p>;


        // let finish = 'won'
        // setHistory([]);}



	return (
		<React.Fragment>
            {/* <Riddle answers={answers} countries={countries} strikes = {strikes} history = {history} finish = {finished}/> */}
            <Riddle answers={answers} countries={countries} strikes = {strikes} history = {history} finished = {finished} headerText = {headerText} classes = {classes} riddleHeaderClass = {riddleHeaderClass}/>
            <Results history = {history} answers = {answers}  finished = {finished} classes = {classes} />
            <Strikes strikes = {strikes} classes = {classes} />
            {showGuess && <Container maxWidth="md" component="main" >
                <Card className={classes.listResults}>
                    <CardContent className={classes.listResults}>

                    {suggestions && suggestions.map((suggestion,i) =>
                        <Typography  
                            key={i} 
                            variant="h6" 
                            color="inherit" 
                            noWrap
                            className = {classes.suggestion}
                            onClick={()=>onSuggestHandler(suggestion.name)}>
                            {suggestion.name}
                        </Typography>
                            )}
                        <form className={classes.guessForm} onSubmit={handleSubmit} >
                            <TextField
                            id="outlined-guess"
                            label="Guess a Country"
                            onChange={e=> onChangeHandler(e.target.value)}
                            value={text}
                            error={boolError}
                            helperText={helpertext}
                            // onBlur={()=> {
                            //     setTimeout(()=>{
                            //         setSuggestions([])
                            //     }, 100)
                            // }}
                            />
                            <Button 
                            className='guessButton'
                            type="submit"
                            variant="contained"
                            disableElevation>
                                Guess
                            </Button>
                            
                        </form>
                    </CardContent>
                </Card>
            </Container>}
		</React.Fragment>
	);
};

export default Game;