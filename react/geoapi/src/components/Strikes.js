import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

const useStyles = makeStyles((theme) => ({
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
    }


}));

const Results = (props) => {

	const {  strikes } = props;


    const classes = useStyles();
    

    return (
		<React.Fragment>                    
            <Container maxWidth="md"  >  
                
            {strikes.map((ans, index) => {   
                return ( 
                    <Card  className= {classes.listResults}>
                        <CardContent className= {classes.listResults}>
                            <li className={classes.incorrect} key={index}>Strike {index+1} : {strikes[index]}</li>
                        </CardContent>
                    </Card>
                    )
                    })}
            </Container>  
        </React.Fragment>
    );
};

export default Results