import * as React from 'react';

import { Socket } from './Socket';
import { ChatBot } from './ChatBot';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();
        var text = document.getElementById('comment').value;
        console.log('Text that was sent: ', text);
        FB.getLoginStatus((response) => {
            if (response.status == 'connected') {
                Socket.emit('new message', {
                    'type': "facebook",
                    'facebook_user_token': response.authResponse.accessToken,
                    'number': text,
                });
            }
            else {
                let auth = gapi.auth2.getAuthInstance();
                let user = auth.currentUser.get();
                if (user.isSignedIn()) {
                    Socket.emit('new message', {
                        'type' : "google",
                        'google_user_token': user.getAuthResponse().id_token,
                        'facebook_user_token': '',
                        'number': text,
                        });
                }

            }
        });
        var toBot = text.split(' ');
        if (toBot[0] == "!!")
        {
            console.log("text should go to bot")
            var Bot = require("./ChatBot");
            Bot.ChattyBot(text);
        }
        document.getElementById('comment').value = ""

    }
    
    

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button id="buttonSend">Send</button>
            </form>
        );
    }
}
