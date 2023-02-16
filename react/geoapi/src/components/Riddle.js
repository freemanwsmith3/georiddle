import React, { useState } from 'react';
import Typography from '@material-ui/core/Typography';
import { Container } from '@material-ui/core';
import {Card} from '@material-ui/core';
import {CardContent} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';



const Riddle = (props) => {
    
    const {finished, answers,  classes, riddleHeaderClass, strikes, guesses} = props;
    
    let headerText = 'Remaining: ' + (answers.answers.length + strikes.length - guesses.length) + ' Countries || ' + (3-strikes.length) + ' Strikes';

    if (finished === 'Lost'){
        headerText = 'You Lost'
    }
    if (finished === 'Won'){
        headerText = 'Winner'
    }
    

    return (
    <React.Fragment>
        <Container maxWidth="md"  >
            <Card className="resultCard">
                <CardContent className="result">
                    <div className={classes.riddleFirst}>
                        <Typography 
                        className={classes.riddleHeader}>
                            GeoRiddle #{answers.id}: {answers.question}
                        </Typography>
                    </div>
                    <div className={classes.riddleSecond}>
                        <Typography 
                        className={riddleHeaderClass}>
                            {headerText}
                        </Typography>
                    </div>
                </CardContent>
            </Card>
        </Container>
    </React.Fragment>
    );
}

export default Riddle
