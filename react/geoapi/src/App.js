import React, { useEffect, useState } from 'react';
import './App.css';

import CountriesLoadingComponent from './components/CountriesLoading';
import axios from 'axios'

import Game from './components/Game';

function App() {
	// const AnswersLoading = AnswersLoadingComponent(Riddle);
	const CountriesLoading = CountriesLoadingComponent(Game)
	// const RiddleLoading = RiddleLoadingComponent(Riddle)

	const startDate = new Date('February 12, 2023 00:00:00');
	const currentDate = new Date();

	const riddleID = Math.ceil((currentDate-startDate)/86400000) // find the riddle id by subtracting the number of days, dividing by milliseconds and rounding up
	const [appState, setAppState] = useState({
		loading: true,
		countries: null,
		answers: null, 
		guesses: null
	});

	useEffect(() => {
		
		setAppState({loading: true});

		//this is where you should load the answers or probably just get rid of it and use a custom hook

		// const loadAnswers = async () => {
		// 	const answerData = await axios.get('http://127.0.0.1:8000/api/riddles/1')
		// 	setAppState({ loadingAnswers: false,  answers: answerData.data});
		// }
		// loadAnswers();

		const loadData = async () => {
			const countryData = await axios.get('http://127.0.0.1:8000/api/countries/');
			const guessData = await axios.get('http://127.0.0.1:8000/api/guesses/' + riddleID);
			const answerData = await axios.get('http://127.0.0.1:8000/api/riddles/' + riddleID);
			setAppState({ loading: false, answers: answerData.data, countries: countryData.data, guesses: guessData.data});
		}
		loadData();

	},[setAppState]);


	return (
		<div className="App">
			{/* <RiddleLoading isLoading={appState.loadingAnswers} answers={appState.answers}/> */}
			{/* <AnswersLoading isLoading={appState.loadingCountries} answers={appState.answers} countries={appState.countries}/> */}
			<CountriesLoading isLoading={appState.loading} answers={appState.answers} countries={appState.countries} guesses={appState.guesses}/>
		</div>
		
	);
}
export default App;