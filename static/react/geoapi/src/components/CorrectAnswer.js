import React, { useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import useGuess from '../hooks/useGuess';
import axios from 'axios';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	countryName: {
		fontSize: '16px',
		textAlign: 'left',
	},
	countryCapital: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Answers = (props) => {

	const { answers } = props;
	//const [ text, setText ] = useState('')
	const { currentGuess, handleKeyup } = useGuess(answers)
	const classes = useStyles();
	//console.log(answers)
	// useEffect(() => {
	// 	const loadanswers = async() => {
	// 		const response = await axios.get('http://127.0.0.1:8000/api/')
	// 	}
	// 	loadanswers();
	// },[])

	// useEffect(() => {
		
	// 	window.addEventListener('keyup', handleKeyup)

	// 	return () => window.removeEventListener('keyup', handleKeyup)
	// }, [handleKeyup])


	if (!answers || answers.length === 0) return <p>Can not find any answers, sorry</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end">
					{answers.map((country) => {
						return (
							// Enterprise card is full width at sm breakpoint
							<Grid item key={country.id} xs={12} md={4}>
								<Card className={classes.card}>
									{/* <CardMedia
										className={classes.cardMedia}
										image="https://source.unsplash.com/random"
										title="Image title"
									/> */}
									<CardContent className={classes.cardContent}>
										<Typography
											gutterBottom
											variant="h6"
											component="h2"
											className={classes.countryName}
										>
											{country.name}
										</Typography>
										<div className={classes.countryCapital}>
											<Typography
												component="p"
												color="textPrimary"
											></Typography>
											<Typography variant="subtitle1" color="textSecondary">
												{country.capital}
											</Typography>
										</div>
									</CardContent>
								</Card>
							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>
	);
};
export default Answers;