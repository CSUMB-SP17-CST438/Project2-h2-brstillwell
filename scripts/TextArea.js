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
        function checker(text)
        {
            Socket.emit("chatroom check", {
                'message': "in chatroom"
            });
            if (text.includes("http") || text.includes(".com") || text.includes(".org") || text.includes(".edu"))
            {
                if (text.includes(".jpg") || text.includes(".gif") || text.includes(".png") || text.includes(".jpeg"))
                    return <img src={text} id="messageImage"/>;
                else 
                    return <a href={text}>{text}</a>;
            }
            else
            return text;
        }
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
                            {checker(n.number)}&nbsp;
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