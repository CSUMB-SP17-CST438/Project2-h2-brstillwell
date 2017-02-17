import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();
        var text = document.getElementById('comment').value;
        console.log(text);
        let random = Math.floor(Math.random() * 100);
        console.log('Generated a random number: ', text);
        Socket.emit('new number', {
            'number': text,
        });
        console.log('Sent up the random number to server!');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Send up a random number!</button>
            </form>
        );
    }
}
