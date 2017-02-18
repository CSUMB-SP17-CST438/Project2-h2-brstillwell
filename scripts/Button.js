import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();
        var text = document.getElementById('comment').value;
        console.log('Text that was sent: ', text);
        Socket.emit('new message', {
            'number': text,
            'username': "TomBot"
        });
        console.log('Sent up the text to server!');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Send</button>
            </form>
        );
    }
}
