import React from 'react';
import { shallow } from 'enzyme';

import App from '../../App';

test('App renders without crashing', async () => {
  const wrapper = shallow(<App />)
});
