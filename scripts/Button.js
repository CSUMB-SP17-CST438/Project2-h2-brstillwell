import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();
        var text = document.getElementById('comment').value;
        console.log('Text that was sent: ', text);
        /*Socket.emit('new message', {
            'number': text,
            'username': "TomBot"
        });*/
        console.log('Sent up the text to server!');
        FB.getLoginStatus((response) => {
            if (response.status == 'connected') {
                Socket.emit('new message', {
                'facebook_user_token': response.authResponse.accessToken,
                'number': text,
                });
            }
        });

    }
    
    

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Send</button>
            </form>
        );
    }
}
