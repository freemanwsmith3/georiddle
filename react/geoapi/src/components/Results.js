import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

const useStyles = makeStyles((theme) => ({
    listResults: {
        padding: '0px',
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


}));

const Results = (props) => {


	const { history, answers } = props;
    const classes = useStyles();

    return (
		<React.Fragment>                    
            <Container maxWidth="md"  >  
                
            {answers.answers.map((ans, index) => {   
                return history.includes(ans.name) ? ( 
                    <Card  className= {classes.listResults} >
                        <CardContent className= {classes.listResults}>
                            <li className={classes.correct} >{ans.name}</li> 
                        </CardContent>
                    </Card>
                ) :(
                    <Card  className= {classes.listResults}>
                        <CardContent className= {classes.listResults}>
                            <li className={classes.blank} key={index}>Country number: {index+1}</li>
                        </CardContent>
                    </Card>
                    )
                    })}
            </Container>  
        </React.Fragment>
    );
};

export default Results