import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField'
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

import Riddle from './Riddle';
import Results from './Results';
import Strikes from './Strikes';

const useStyles = makeStyles((theme) => ({
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
    }


}));

const Guess = (props) => {

    const { answers, countries } = props;
    const [strikes] = useState([])
	const [text, setText] = useState([])
    const [suggestions, setSuggestions] = useState([])
    const [history, setHistory] = useState([])
    const [finished, setFinished] = useState([])
    const [boolError, setBoolError] = useState(false)
    const [helpertext, setHelpertext] = useState([])


    
    const classes = useStyles();
    

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
        let submittedText = text.trim()

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
        console.log(countryValidation.length)
        if (countryValidation.length===0){
            setBoolError(true)
            setHelpertext('Enter a valid country')
            setText('')

            return
        }
        history.push(submittedText)


        let isStrike = true
        for (var i = 0; i < answers.answers.length; i++){
            if (answers.answers[i].name === submittedText){
                isStrike = false
            }

        }

        if (isStrike === true){
            strikes.push(submittedText)
            setText('')
            return
        }
        setText('')
        return
    }

	if (!answers || answers.length === 0) return <p>Can not find any answers, sorry</p>;

    if ((answers.answers.length+strikes.length-history.length)===0 ){
        // let finish = 'won'
        // setHistory([]);
    return(
        <React.Fragment>
            <div>
                You've Won
            </div>
            {/* <Riddle answers={answers} countries={countries} strikes = {strikes} history = {history}/> */}
            {/* <Results history = {history} answers = {answers}/> */}
        </React.Fragment>
    )}

    if  (strikes.length===3) {
        // let finish = 'lost'
        // setHistory([]);
    return(
        <React.Fragment>
            <div>
                You lost
            </div>
            {/* <Riddle answers={answers} countries={countries} strikes = {strikes} history = {history} /> */}
            {/* <Results history = {history} answers = {answers}/> */}
        </React.Fragment>
        
    )}
	return (
		<React.Fragment>
            {/* <Riddle answers={answers} countries={countries} strikes = {strikes} history = {history} finish = {finished}/> */}
            <Riddle answers={answers} countries={countries} strikes = {strikes} history = {history} />
            <Results history = {history} answers = {answers}/>
            <Strikes strikes = {strikes}  />
            <Container maxWidth="md" component="main" >
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



            </Container>
		</React.Fragment>
	);
};

export default Guess;