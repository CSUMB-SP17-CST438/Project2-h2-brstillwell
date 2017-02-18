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
        Socket.on('chatroom', (data) => {
            this.setState({
                'numbers': data['numbers']
                
            });
        })
    }

    render() {
        /*let numbers = this.state.numbers.map(
            (n, index) => <td key={index}>{n}</td>
        );
        let username = this.state.usernames.map(
            (u, index) => <td key={index}>{u} says:</td>
        );*/
        let numbers = this.state.numbers.map((n, index) =>
        <table key={index}>
            <tbody >
                <tr>
                    <td rowSpan="2" id="images">
                        <img src={n.picture}/>
                    </td>
                    <td>
                        {n.name} says:
                    </td>
                </tr>
                <tr>
                    <td>
                        {n.number}
                    </td>
                </tr>
            </tbody>
        </table>
         );

        /*function printMessages() {
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
        }*/
        
        return(
        <div id="chatBox">
                    {numbers}
        </div>
        );
    }
}
//var mylist = document.getElementById("myList");
//document.getElementById("favorite").value = mylist.options[mylist.selectedIndex].text;