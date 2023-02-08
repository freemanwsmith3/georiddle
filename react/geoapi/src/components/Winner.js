import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField'
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';

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

    correct: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '24px',
        textAlign: 'center',
        marginBottom: theme.spacing(2),
        color: 'green'
    },

    incorrect: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'baseline',
        fontSize: '24px',
        textAlign: 'center',
        marginBottom: theme.spacing(2),
        color: 'red'
    }, 


}));

const Guess = (props) => {
    const [results, setResults] = useState([])
	const [text, setText] = useState([])
    const [suggestions, setSuggestions] = useState([])
    const [history, setHistory] = useState([])
    const [boolError, setBoolError] = useState(false)
    const [helpertext, setHelpertext] = useState([])
	const { answers } = props;
    const { countries } = props;
    const classes = useStyles();

	return (
		<React.Fragment>

			<Container maxWidth="md" component="main" >
                {results.map((visible, index) => {    
                    return visible ? ( 
                        <li  className={classes.correct} key = {index}>{history[index]}</li> 
                        ) :(
                        <li  className={classes.incorrect} key = {index}>{history[index]}</li>
                    )
                })}
                <Card className="guessCard">
                    <CardContent className="guess">

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