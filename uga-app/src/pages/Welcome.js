import '../styles/landing.css';
import BounceTitle from './components/BounceTitle';
import {Link} from "react-router-dom";
import { selectUser } from '../redux-slices/UserSlice';
import { useSelector } from 'react-redux';

function Welcome() {
  const user = useSelector(selectUser);
  let text = "Let's get started";
  if (user != null) { 
    text = "View Your Dashboard"
  }
  return (
    <div style={{
      justifyContent: 'center',
      display: 'flex',
      margin: 'auto',
      marginTop: '109px',
    }}>
      <div>
        <BounceTitle/>
        <div class="bg" style={{marginTop: '225px'}}>
          <Link to="/login" className='start'>{text}</Link>
        </div>
      </div>
    </div>
  );
}

export default Welcome;
