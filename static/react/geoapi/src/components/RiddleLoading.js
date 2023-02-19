import React from 'react';

function RiddleLoading(Component) {
	return function RiddleLoadingComponent({ isLoading, ...props }) {
		if (!isLoading) return <Component {...props} />;
		return (
			<p style={{ fontSize: '25px' }}>
				Loading today's riddle
			</p>
		);
	};
}
export default RiddleLoading


