import { configureStore } from '@reduxjs/toolkit'
import { userReducer } from './redux-slices/UserSlice'

export default configureStore({
  reducer: {
      user: userReducer
  }
})