import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import $ from 'jquery'

function App() {
	const [message, setMessage] = useState({})

	$.ajaxSetup({
		crossDomain: true
	})
	const query = async () => {
		var request = '/api/1' // This should be passed in as an arg
		var uri = 'http://127.0.0.1:5000' + request
		console.log(uri)
		
		$.getJSON({url: uri, crossDomain: true}, function(data){
			console.log("Response: ", data)
			setMessage(data)
		})
	}
	
	useEffect(()=>{
		query()
	}, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          React + Flask = (this)
        </p>
		<h3>{message.name}</h3> 
      </header>
    </div>
  );
}

export default App;