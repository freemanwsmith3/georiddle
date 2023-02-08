import React, { useEffect, useState } from 'react';
import './App.css';

import CountriesLoadingComponent from './components/CountriesLoading';
import axios from 'axios'

import Game from './components/Game';

function App() {
	// const AnswersLoading = AnswersLoadingComponent(Riddle);
	const CountriesLoading = CountriesLoadingComponent(Game)
	// const RiddleLoading = RiddleLoadingComponent(Riddle)
	const [appState, setAppState] = useState({
		loadingAnswers: true,
		loadingCountries: true,
		countries: null,
		answers: null
	});

	useEffect(() => {
		setAppState({ loadingAnswers: true,  loadingCountries: true });

		//this is where you should load the answers or probably just get rid of it and use a custom hook

		// const loadAnswers = async () => {
		// 	const answerData = await axios.get('http://127.0.0.1:8000/api/riddles/1')
		// 	setAppState({ loadingAnswers: false,  answers: answerData.data});
		// }
		// loadAnswers();

		const loadCountries = async () => {
			const countryData = await axios.get('http://127.0.0.1:8000/api/countries/')
			const answerData = await axios.get('http://127.0.0.1:8000/api/riddles/1')
			setAppState({ loadingCountries: false, answers: answerData.data, countries: countryData.data});
		}
		loadCountries();

	},[setAppState]);


	return (
		<div className="App">
			{/* <RiddleLoading isLoading={appState.loadingAnswers} answers={appState.answers}/> */}
			{/* <AnswersLoading isLoading={appState.loadingCountries} answers={appState.answers} countries={appState.countries}/> */}
			<CountriesLoading isLoading={appState.loadingCountries} answers={appState.answers} countries={appState.countries}/>
		</div>
		
	);
}
export default App;