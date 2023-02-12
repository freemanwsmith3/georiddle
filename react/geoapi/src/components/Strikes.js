import React from 'react';
// import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';


const Results = (props) => {

	const {  strikes, classes } = props;

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