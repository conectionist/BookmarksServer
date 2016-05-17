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
public class InvalidParameterException extends Exception {
    protected String parameterName;

    public InvalidParameterException(String parameterName) {
        this.parameterName = parameterName;
    }

    public String getInvalidParameterName() {
        return parameterName;
    }
}
