import React from 'react';

import Container from '@material-ui/core/Container';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';


const Results = (props) => {


	const { history, answers, finished, classes } = props;

    if (finished === 'Won' || finished === 'Lost'){
        for (var i = 0; i < answers.answers.length; i++){
            history.push(answers.answers[i].name)
        }
    }
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
                            <li className={classes.blank} key={index}>Country Number: {index+1}</li>
                        </CardContent>
                    </Card>
                    )
                    })}
            </Container>  
        </React.Fragment>
    );
};

export default Results