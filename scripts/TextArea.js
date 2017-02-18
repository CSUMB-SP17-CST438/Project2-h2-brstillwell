import * as React from 'react';

import { Socket } from './Socket';


export class TextArea extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': [],
            'usernames': [],
            'messages': [],
        };
    }

    componentDidMount() {
        Socket.on('chatroom', (data) => {
            this.setState({
                'numbers': data['numbers'],
                'usernames': data['username']
                
            });
        })
    }

    render() {
        let numbers = this.state.numbers.map(
            (n, index) => <td key={index}>{n}</td>
        );
        let username = this.state.usernames.map(
            (u, index) => <td key={index}>{u} says:</td>
        );
        function printMessages() {
            console.log("this is the function i created - number: " + numbers.length)
            var results = [];
            for (var i=0; i < numbers.length; i++) {
                results.push(
                    
                <table key={i}>
                    <tbody>
                        <tr>
                            <td rowSpan="2" id="images">
                                <img src="static/tom2.jpg"/>
                            </td>
                            {username[i]}
                        </tr>
                        <tr>
                            {numbers[i]}

                        </tr>
                    </tbody>
                </table>)
            }
            return results;
        }
        
        return(
        <div id="chatBox">
                    {printMessages()}
        </div>
        );
    }
}
//var mylist = document.getElementById("myList");
//document.getElementById("favorite").value = mylist.options[mylist.selectedIndex].text;