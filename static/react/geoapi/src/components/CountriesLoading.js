import React from 'react';

function CountriesLoading(Component) {
	
	return function CountriesLoadingComponent({ isLoading, ...props }) {
		if (!isLoading) return <Component {...props} />;
		return (
			<p style={{ fontSize: '25px' }}>
				Fetching answers...
			</p>
		);
	};
}
export default CountriesLoading;