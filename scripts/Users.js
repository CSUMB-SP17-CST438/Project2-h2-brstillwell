import * as React from 'react';

import { Socket } from './Socket';


export class Users extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': []
        };
        
    }
    componentDidMount() {
        Socket.on('userList', (data) => {
            this.setState({
                'numbers': data['numbers']
                
            });
        })
    }
    
    render(){
        function test() {
            Socket.emit("chatroom check", {
                'message': "in chatroom"
            });
        }
        let numbers = this.state.numbers.map((n, index) =>
        <table key={index}>
            <tbody >
                <tr>
                    <td id="images2">
                        <img src={n.picture} id="avatar"/>
                    </td>
                        <td id="message2">
                            <div  id="name">
                                {n.name}
                            </div>
                    </td>
                </tr>
            </tbody>
        </table>
         );
        return(
            <div>
                {numbers}
                {test()}
            </div>
            );
    }
}
/*FB.getLoginStatus((response) => {
                        if (response.status == 'connected') {
                            console.log("there is a new user");
                            Socket.emit('new user', {
                                'facebook_user_token': response.authResponse.accessToken
                            });
                        }
                    });*/