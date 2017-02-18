import * as React from 'react';

import { Button } from './Button';
import { TextArea } from './TextArea';

export class Content extends React.Component {
    render() {
        return (
            <div>
                <h1>Chat Room: </h1>
                <TextArea />
            
                <div className="form-group">
                    <label htmlFor="comment"></label>
                        <input type="text" placeholder="Type a message" id="comment"/> 
                    <Button />
                </div>
            </div>
        );
    }
}
