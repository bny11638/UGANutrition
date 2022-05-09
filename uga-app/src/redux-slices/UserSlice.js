import { createSlice} from "@reduxjs/toolkit";

// Bundle of Reducer functions for UserSlice
export const UserSlice = createSlice({
    name: 'user',
    initialState: {
        value: null
    },
    // functions that can change the "user".value
    reducers: {
        login: (state, action) => {
            state.value = action.payload;
        },
        logout: (state, action) => {
            state.value = null;
        }
    }
})

//Selector function for getting user value
export const selectUser = (state) => state.user.value; 
export const {login, logout} = UserSlice.actions;
export const  userReducer =  UserSlice.reducer;