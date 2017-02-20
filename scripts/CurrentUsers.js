import * as React from 'react';

import { Socket } from './Socket';


export class CurrentUsers extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'current': []
        };
    }
    componentDidMount() {
        Socket.on('usersCount', (data) => {
            this.setState({
                'current': data
            });
            console.log("This is the number: " + data['users'])
        })
    }
    
    render(){
        let current = this.state.current
        return(
            <h1>Current Users: {current}</h1>
            );
    }
}