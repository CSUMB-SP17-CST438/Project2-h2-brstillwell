import * as React from 'react';

import { Button } from './Button';
import { TextArea } from './TextArea';

export class Content extends React.Component {

    render() {
        return (
            <div>
                <h1>Random numbers: </h1>
                <TextArea />
                <Button />
            
                <div class="form-group">
                    <label for="comment">Comment:</label>
                    <textarea class="form-control" rows="1" id="comment"></textarea>
                </div>
            </div>
        );
    }
}
