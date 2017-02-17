import * as React from 'react';

import { Socket } from './Socket';


export class TextArea extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': []
        };
    }

    componentDidMount() {
        Socket.on('all numbers', (data) => {
            this.setState({
                'numbers': data['numbers']
            });
        })
    }

    render() {
        let numbers = this.state.numbers.map(
            (n, index) => <li key={index}>{n}</li>
                
        );
        return(
        <div id="chats">
            <ul>
                {numbers}
            </ul>
        </div>
        );
    }
}
//var mylist = document.getElementById("myList");
//document.getElementById("favorite").value = mylist.options[mylist.selectedIndex].text;