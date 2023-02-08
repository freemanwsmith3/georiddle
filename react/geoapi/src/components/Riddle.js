import React from 'react';

import Typography from '@material-ui/core/Typography';
import { Container } from '@material-ui/core';
import {Card} from '@material-ui/core';
import {CardContent} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

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
    }
}));

const Riddle = (props) => {

    const {answers, strikes, history} = props;
    const classes = useStyles();

    return (
    <React.Fragment>
        <Container maxWidth="md"  >
            <Card className="resultCard">
                <CardContent className="result">
                    <div className={classes.riddleFirst}>
                        <Typography 
                        className={classes.riddleHeader}>
                            {answers.question}
                        </Typography>
                    </div>
                    <div className={classes.riddleSecond}>
                        <Typography 
                        className={classes.riddleNumberOfCountries}>
                   Remaining: {answers.answers.length+strikes.length-history.length} Countries  || {3 -strikes.length} Strikes
                        </Typography>
                    </div>
                </CardContent>
            </Card>
        </Container>
    </React.Fragment>
    );
}

export default Riddle
