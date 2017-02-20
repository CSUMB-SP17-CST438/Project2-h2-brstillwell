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
        let numbers = this.state.numbers.map((n, index) =>
        <table key={index}>
            <tbody >
                <tr>
                    <td rowSpan="2" id="images">
                        <img src={n.picture} id="avatar"/>
                    </td>
                        <td id="message">
                            <div  id="name">
                                {n.name} says:
                            </div>
                        <br />
                        <div>
                            {n.number}&nbsp;
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
         );
        
        return(
        <div id="chatBox">
                    {numbers}
        </div>
        );
    }
}
//var mylist = document.getElementById("myList");
//document.getElementById("favorite").value = mylist.options[mylist.selectedIndex].text;