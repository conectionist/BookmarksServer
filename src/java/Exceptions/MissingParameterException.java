/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Exceptions;

/**
 *
 * @author Dan
 */
public class MissingParameterException extends Exception {
    protected String parameterName;

    public MissingParameterException(String parameterName) {
        this.parameterName = parameterName;
    }

    public String getMissingParameterName() {
        return parameterName;
    }
    
    
}
